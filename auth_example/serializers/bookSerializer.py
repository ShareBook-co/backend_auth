from rest_framework.relations      import PrimaryKeyRelatedField
from auth_example.models.author    import Author
from auth_example.models.book      import Book
from auth_example.models.grade     import Grade
from auth_example.models.editorial import Editorial
from rest_framework                import serializers
from auth_example.models.user      import User


class BookSerializer(serializers.ModelSerializer):
    editorial = PrimaryKeyRelatedField(queryset=Editorial.objects.all())
    grade     = PrimaryKeyRelatedField(queryset=Grade.objects.all())
    author    = PrimaryKeyRelatedField(queryset=Author.objects.all(),many=True)
    user      = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Book
        fields = ['id_book', 'isbn', 'title', 'language', 'price', 
                  'state', 'editorial', 'grade', 'author', 'user']
    
    def create(self, validated_data):
        author   = validated_data.pop("author")
        instance = Book.objects.create(**validated_data)
        instance.author.set(author)
        return instance

    def to_representation(self, obj):
        book      = Book.objects.get(id_book=obj.id_book)
        editorial = Editorial.objects.get(id_editorial=obj.editorial_id)
        grade     = Grade.objects.get(id_grade=obj.grade_id)
        user      = User.objects.get(id=obj.user_id)

        authors = []
        for author in obj.author.all():
            authors.append(author.name_author)

        return {
            'id_book':   book.id_book,
            'isbn':      book.isbn,
            'title':     book.title,
            'language':  book.language,
            'price':     book.price,
            'state':     book.state,
            'editorial': editorial.name_editorial,
            'grade':     grade.name_grade,
            'author':    authors,
            'user':      user.name,
        }
