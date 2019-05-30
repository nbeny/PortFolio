from djongo import models
from django import forms

length = 255

FILE_PATH_IMAGE = './Data/Image/'
FILE_PATH_TORRENT = './Data/Torrent/'


class Film(models.Model):
    _id = models.ObjectIdField(primary_key=True)

    Title = models.CharField(max_length=length, blank=True, null=True)
    Image = models.FilePathField(path=FILE_PATH_IMAGE, blank=True, null=True)

    WeightTorrent = models.FilePathField(max_length=length, blank=True, null=True)

    Categorie = models.CharField(max_length=length, blank=True, null=True)
    CategorieDown = models.CharField(max_length=length, blank=True, null=True)

    FileName = models.CharField(max_length=length, blank=True, null=True)
    Quality = models.CharField(max_length=length, blank=True, null=True)
    Description = models.CharField(max_length=length, blank=True, null=True)

    Seed = models.CharField(max_length=length, blank=True, null=True)
    Leech = models.CharField(max_length=length, blank=True, null=True)
    TorrentDownload = models.CharField(path=FILE_PATH_TORRENT, blank=True, null=True)

    CreationDate = models.DateTimeField(blank=True, null=True)
    UpdateDate = models.DateTimeField(blank=True, null=True)
    DateTime = models.DateTimeField(auto_now_add=True, null=True)

    objects = models.DjongoManager()


    def __str__(self):
        return "{}".format(self.Title)