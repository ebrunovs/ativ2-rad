from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import Livro, Editora, Autor
import random
from decimal import Decimal


class Command(BaseCommand):
    help = 'Gera 100 registros de livros com dados fictícios usando Faker'

    def add_arguments(self, parser):
        parser.add_argument(
            '--quantidade',
            type=int,
            default=100,
            help='Quantidade de livros a serem criados (padrão: 100)'
        )

    def handle(self, *args, **options):
        fake = Faker('pt_BR')  # Usando locale brasileiro
        quantidade = options['quantidade']
        
        self.stdout.write(self.style.WARNING(f'Iniciando geração de {quantidade} livros...'))
        
        # Verificar se existem editoras, caso contrário criar algumas
        if Editora.objects.count() == 0:
            self.stdout.write(self.style.NOTICE('Nenhuma editora encontrada. Criando editoras...'))
            editoras_nomes = [
                'Editora Companhia das Letras',
                'Editora Record',
                'Editora Globo',
                'Editora Saraiva',
                'Editora Rocco',
                'Editora Intrínseca',
                'Editora Arqueiro',
                'Editora Suma',
                'Editora Aleph',
                'Editora DarkSide',
            ]
            for nome in editoras_nomes:
                Editora.objects.get_or_create(nome=nome)
            self.stdout.write(self.style.SUCCESS(f'✓ {len(editoras_nomes)} editoras criadas'))
        
        # Verificar se existem autores, caso contrário criar alguns
        if Autor.objects.count() == 0:
            self.stdout.write(self.style.NOTICE('Nenhum autor encontrado. Criando autores...'))
            for _ in range(30):
                nome = fake.name()
                Autor.objects.get_or_create(nome=nome)
            self.stdout.write(self.style.SUCCESS(f'✓ 30 autores criados'))
        
        # Obter todas as editoras disponíveis
        editoras = list(Editora.objects.all())
        
        if not editoras:
            self.stdout.write(self.style.ERROR('❌ Erro: Nenhuma editora disponível no banco de dados'))
            return
        
        # Contador de livros criados
        livros_criados = 0
        livros_duplicados = 0
        
        # Gerar livros
        for i in range(quantidade):
            try:
                # Gerar ISBN único (13 dígitos)
                isbn = fake.isbn13(separator="")
                
                # Verificar se ISBN já existe
                if Livro.objects.filter(ISBN=isbn).exists():
                    livros_duplicados += 1
                    # Gerar novo ISBN até encontrar um único
                    tentativas = 0
                    while Livro.objects.filter(ISBN=isbn).exists() and tentativas < 10:
                        isbn = fake.isbn13(separator="")
                        tentativas += 1
                    
                    if tentativas >= 10:
                        continue
                
                # Gerar título do livro (2-5 palavras)
                titulo = fake.catch_phrase()
                
                # Gerar data de publicação (últimos 30 anos)
                publicacao = fake.date_between(start_date='-30y', end_date='today')
                
                # Gerar preço entre R$ 19.90 e R$ 299.90
                preco = Decimal(random.uniform(19.90, 299.90)).quantize(Decimal('0.01'))
                
                # Gerar estoque entre 0 e 500
                estoque = random.randint(0, 500)
                
                # Selecionar editora aleatória
                editora = random.choice(editoras)
                
                # Criar o livro
                livro = Livro.objects.create(
                    ISBN=isbn,
                    titulo=titulo,
                    publicacao=publicacao,
                    preco=preco,
                    estoque=estoque,
                    editora=editora
                )
                
                livros_criados += 1
                
                # Mostrar progresso a cada 10 livros
                if (i + 1) % 10 == 0:
                    self.stdout.write(
                        self.style.SUCCESS(f'✓ {livros_criados}/{quantidade} livros criados...')
                    )
            
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'❌ Erro ao criar livro {i+1}: {str(e)}')
                )
        
        # Mensagem final
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS(f'✅ Geração concluída com sucesso!'))
        self.stdout.write(self.style.SUCCESS(f'📚 Total de livros criados: {livros_criados}'))
        if livros_duplicados > 0:
            self.stdout.write(self.style.WARNING(f'⚠️  ISBNs duplicados evitados: {livros_duplicados}'))
        self.stdout.write(self.style.SUCCESS(f'🏢 Editoras disponíveis: {len(editoras)}'))
        self.stdout.write(self.style.SUCCESS(f'📖 Total de livros no banco: {Livro.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.NOTICE(f'\n💡 Acesse http://localhost:8000/blog/livros/ para ver a paginação'))
