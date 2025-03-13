# Generated by Django 5.1.4 on 2025-03-12 04:43

import django.db.models.deletion
import pgvector.django.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("knowledge", "0002_remove_part_unique_part_identifier_per_page_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="vectorstore",
            name="unique_vector_per_part",
        ),
        migrations.AddField(
            model_name="vectorstore",
            name="content",
            field=models.TextField(
                default="dummy", help_text="The content that was embedded"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="vectorstore",
            name="embedding_model",
            field=models.CharField(
                choices=[
                    ("ada002", "text-embedding-ada-002"),
                    ("minilm", "all-MiniLM-L6-v2"),
                    ("mpnet", "all-mpnet-base-v2"),
                    ("bger", "bge-large-en"),
                    ("voyage", "voyage-multimodal-3"),
                ],
                help_text="Must match the embedding model in agent settings",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="vectorstore",
            name="part",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vectors",
                to="knowledge.part",
            ),
        ),
        migrations.AddIndex(
            model_name="vectorstore",
            index=pgvector.django.indexes.HnswIndex(
                ef_construction=64,
                fields=["vector"],
                m=16,
                name="vector_index",
                opclasses=["vector_cosine_ops"],
            ),
        ),
        migrations.AddConstraint(
            model_name="vectorstore",
            constraint=models.UniqueConstraint(
                fields=("part",), name="unique_vector_per_part"
            ),
        ),
    ]
