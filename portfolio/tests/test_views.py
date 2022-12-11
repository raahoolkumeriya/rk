from django.test import TestCase
from portfolio.views import IndexListView
from django.urls import reverse,resolve
from portfolio.models import Projects, AwardsAndAchievements, Summary,\
    Experience, Notes, Contact


class IndexListViewTestCase(TestCase):
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
        AwardsAndAchievements.objects.create(
            title='Test Award',
            received='2022-02-22')
        Summary.objects.create(
            summary='Test Summary',
            summary_image='http://test.com',
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/index.html')

    def test_get_model_data_empty(self):
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['project_list'].count(), 1)
        self.assertEqual(response.context['award_list'].count(), 1)
        self.assertEqual(response.context['summary_list'].count(), 1)


    def test_get_model_data_not_empty(self):
        Projects.objects.create(
            title='Test Project 2',
            summary='Test Summary 2',
            slug='test-project-2',
            category='test-category-2',
            urllink='http://test-2.com',
            startdate='2022-02-22',
            enddate='2022-02-22',
            technology='test-technology-2',
            sourcecode='http://test-2.com',
            description='Test Description 2',
            image='http://test-2.com',
            publish=True,
            pub_date='2022-02-22')
        AwardsAndAchievements.objects.create(
            title='Test Award 2',
            received='2022-02-22')
        Summary.objects.create(
            summary='Test Summary 2',
            summary_image='http://test-2.com',
        )
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['project_list'].count(), 2)
        self.assertEqual(response.context['award_list'].count(), 2)
        self.assertEqual(response.context['summary_list'].count(), 2)


class ProjectListViewTestCase(TestCase):
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

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('portfolio:project-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:project-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/project_list.html')

    def test_get_model_data_empty(self):
        response = self.client.get(reverse('portfolio:project-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['project_list'].count(), 1)

    def test_get_model_data_not_empty(self):
        Projects.objects.create(
            title='Test Project 2',
            summary='Test Summary 2',
            slug='test-project-2',
            category='test-category-2',
            urllink='http://test-2.com',
            startdate='2022-02-22',
            enddate='2022-02-22',
            technology='test-technology-2',
            sourcecode='http://test-2.com',
            description='Test Description 2',
            image='http://test-2.com',
            publish=True,
            pub_date='2022-02-22')
        response = self.client.get(reverse('portfolio:project-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['project_list'].count(), 2)


class NoteListViewTestCase(TestCase):
    def setUp(self):
        Notes.objects.create(
            note='Test Note',
            description='Test Note',
            tags='Test Note',
            gisturl='Test Note')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/notes/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('portfolio:note-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:note-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/note.html')

    def test_get_model_data_empty(self):
        response = self.client.get(reverse('portfolio:note-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['note_list'].count(), 1)


class ProjectDetailViewTestCase(TestCase):
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

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/projects/test-project/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('portfolio:project-detail', args=('test-project',)))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:project-detail', args=('test-project',)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/project_detail.html')
        
    def test_get_model_data_empty(self):
        response = self.client.get(reverse('portfolio:project-detail', args=('test-project',)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['projects'].title, 'Test Project')


class ExperienceListViewTestCase(TestCase):
    def setUp(self):
        Experience.objects.create(
            title='Test Experience',
            start_date='2022-02-22',
            end_date='2022-02-22',
            experience='Test Description',
            )
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/experience/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('portfolio:experience-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:experience-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/experience.html')

    def test_get_model_data_empty(self):
        response = self.client.get(reverse('portfolio:experience-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['experience_list'].count(), 1)


class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(
            email='Test@email.com',
            subject='Test Contact',
            message_date="2022-02-22",
            message='Test Contact',
            )
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/contact.html')
