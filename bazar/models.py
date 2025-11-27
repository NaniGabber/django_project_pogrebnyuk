from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    class Meta:
        ordering = ("title", "open_time")
        verbose_name = "Секція"
        verbose_name_plural = "Секції"

    title = models.CharField(max_length=64)
    position = models.CharField(max_length=255)
    is_required_sale_license = models.BooleanField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    slug = models.SlugField(default="", null=False, editable=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            UKR_TRANSLIT_TABLE = {
                "а": "a",
                "б": "b",
                "в": "v",
                "г": "h",
                "ґ": "g",
                "д": "d",
                "е": "e",
                "є": "ie",
                "ж": "zh",
                "з": "z",
                "и": "y",
                "і": "i",
                "ї": "i",
                "й": "i",
                "к": "k",
                "л": "l",
                "м": "m",
                "н": "n",
                "о": "o",
                "п": "p",
                "р": "r",
                "с": "s",
                "т": "t",
                "у": "u",
                "ф": "f",
                "х": "kh",
                "ц": "ts",
                "ч": "ch",
                "ш": "sh",
                "щ": "shch",
                "ь": "",
                "ю": "iu",
                "я": "ia",
                "А": "A",
                "Б": "B",
                "В": "V",
                "Г": "H",
                "Ґ": "G",
                "Д": "D",
                "Е": "E",
                "Є": "Ye",
                "Ж": "Zh",
                "З": "Z",
                "И": "Y",
                "І": "I",
                "Ї": "Yi",
                "Й": "Y",
                "К": "K",
                "Л": "L",
                "М": "M",
                "Н": "N",
                "О": "O",
                "П": "P",
                "Р": "R",
                "С": "S",
                "Т": "T",
                "У": "U",
                "Ф": "F",
                "Х": "Kh",
                "Ц": "Ts",
                "Ч": "Ch",
                "Ш": "Sh",
                "Щ": "Shch",
                "Ь": "",
                "Ю": "Iu",
                "Я": "Ia",
            }

            table = str.maketrans(UKR_TRANSLIT_TABLE)
            slug = self.title.translate(table)

            self.slug = slugify(slug)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    class Meta:
        ordering = ("title", "product_qty")
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

    title = models.CharField(max_length=255)
    price = models.FloatField()
    product_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    section_located = models.ForeignKey(Section, on_delete=models.CASCADE)
    slug = models.SlugField(default="", null=False, editable=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            temp = self.title.translate(
                str.maketrans(
                    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                    "abvgdeejzijklmnoprstufhzcss_y_eua",
                )
            )
            self.slug = slugify(temp)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
