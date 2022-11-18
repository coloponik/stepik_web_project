from django_seed import Seed
from qa.models import Question, Answer

seeder = Seed.seeder()

seeder.add_entity(Question, 10)
seeder.add_entity(Answer, 20)

seeder.execute()