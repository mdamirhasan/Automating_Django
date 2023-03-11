from django.test import TestCase

# Create your tests here.
import pytest    
from app.models import Contact    

@pytest.mark.django_db #give test access to database  
def test_contact_create():    
    # Create dummy data       
    contact = Contact.objects.create(full_name="Muhammed Ali", phone_number="75859538350",)    
    # Assert the dummy data saved as expected       
    assert contact.full_name=="Muhammed Ali"      
    assert contact.phone_number=="75859538350"
