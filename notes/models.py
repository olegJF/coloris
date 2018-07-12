from django.db import models


class Note(models.Model):
    text = models.TextField(verbose_name='Содержимое заметки')
    timestamp = models.DateTimeField(auto_now_add=True)
    unique_words = models.PositiveIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-unique_words']

    def __str__(self):
        if len(self.text) <= 20:
            return self.text
        else:
            return self.text[: 20] + '....'
            
    def save(self, *args, **kwargs):
            words = set(self.text.lower().split(' '))
            self.unique_words = len(words)
            super().save(*args, **kwargs)
        
    
