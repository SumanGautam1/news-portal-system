from django.db import models


class Heading(models.Model):
    """
    Represents a heading with a title, image, and description.

    Attributes:
        title (CharField): The title of the heading, limited to 20 characters.
        image (ImageField): An image associated with the heading, uploaded to the 'image' directory.
        desc (CharField): A short description of the heading, limited to 200 characters.
    """
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image')
    desc = models.CharField(max_length=200)


class Feedback(models.Model):
    """
    Represents user feedback with a name, email, description, and optional image.

    Attributes:
        name (CharField): The name of the user providing feedback, limited to 20 characters.
        email (EmailField): The email address of the user providing feedback.
        desc (CharField): The feedback description, limited to 200 characters.
        image (ImageField): An optional image uploaded by the user, stored in the 'image' directory.
    """
    name = models.CharField(max_length=20)
    email = models.EmailField()
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image', blank=True)


class Government(models.Model):
    """
    Represents a government-related entity with an image, title, description, and source.

    Attributes:
        image (ImageField): An image representing the government entity, uploaded to the 'image' directory.
        title (CharField): The title of the government entity, limited to 50 characters.
        about (TextField): A detailed description of the government entity.
        source (CharField): The source or origin of the information, limited to 50 characters.
    """
    image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=50)
    about = models.TextField()
    source = models.CharField(max_length=50)
    