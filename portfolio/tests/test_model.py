from django.test import TestCase
from portfolio.models import Projects, AwardsAndAchievements, Notes, Summary,\
    Experience, Contact


class ProjectsTestCase(TestCase):
    def setUp(self):
        Projects.objects.create(
            title='Test Project',
            summary='Test Summary',
            slug='test-project',
            category='test-category',
            urllink='http://test.com',
            startdate='2022-02-22',
            enddate='2022-02-22',
            technology='test-technology',
            sourcecode='http://test.com',
            description='Test Description',
            image='http://test.com',
            publish=True,
            pub_date='2022-02-22')

    def test_project_title(self):
        """Test correct project get created"""
        project = Projects.objects.get(title='Test Project')
        self.assertEqual(project.title, 'Test Project')

    def test_project_summary(self):
        """Test correct project get created"""
        project = Projects.objects.get(title='Test Project')
        self.assertEqual(project.summary, 'Test Summary')
    
    def test_was_published_recently(self):
        """Test correct project get created"""
        project = Projects.objects.get(title='Test Project')
        self.assertEqual(project.was_published_recently(), True)

    def test_project_readtime(self):
        """Test correct project get created"""
        project = Projects.objects.get(title='Test Project')
        self.assertEqual(project.get_readtime(), '1 min')

    
class AwardsAndAchievementsTestCase(TestCase):
    def setUp(self):
        AwardsAndAchievements.objects.create(
            title='Test Award',
            received='2022-02-22')

    def test_award_title(self):
        """Test correct award get created"""
        award = AwardsAndAchievements.objects.get(title='Test Award')
        self.assertEqual(award.title, 'Test Award')
    
    def test_get_formated_date(self):
        """Test correct award get created"""
        award = AwardsAndAchievements.objects.get(title='Test Award')
        self.assertEqual(award.get_formated_date(), 'February 2022')


class NotesTestCase(TestCase):
    def setUp(self):
        Notes.objects.create(
            note='Test Note',
            description='Test Note',
            tags='Test Note',
            gisturl='Test Note')

    def test_note_title(self):
        """Test correct note get created"""
        note = Notes.objects.get(note='Test Note')
        self.assertEqual(note.note, 'Test Note')


class SummaryTestCase(TestCase):
    def setUp(self):
        Summary.objects.create(
            summary='Test Summary',
            summary_image='http://test.com',
          )

    def test_summary_title(self):
        """Test correct summary get created"""
        summary = Summary.objects.get(summary='Test Summary')
        self.assertEqual(summary.summary, 'Test Summary')


class ExperienceTestCase(TestCase):
    def setUp(self):
        Experience.objects.create(
            title='Test Experience',
            start_date='2022-02-22',
            end_date='2022-02-22',
            experience='Test Description',
            )
        
    def test_experience_creation(self):
        """Test correct experience get created"""
        experience = Experience.objects.get(title='Test Experience')
        self.assertEqual(experience.title, 'Test Experience')


class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(
            email='Test@email.com',
            subject='Test Contact',
            message_date="2022-02-22",
            message='Test Contact',
            )

    def test_contact_creation(self):
        """Test correct contact get created"""
        contact = Contact.objects.get(email='Test@email.com')
        self.assertEqual(contact.email, 'Test@email.com')