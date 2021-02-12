from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, DecimalField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore, ItemCategory


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # Adds the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button

    title = StringField(
        'Store Title',
        validators=[DataRequired(), Length(min=3, max=80)]
        )
    address = StringField(
        'Store Address',
        validators=[DataRequired(), Length(min=10, max=120)]
        )
    submit = SubmitField('Submit')


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # Adds the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button

    name = StringField(
        'Item Name',
        validators=[DataRequired(), Length(min=3, max=80)]
        )
    price = DecimalField(
        'Item Price',
        validators=[DataRequired()]
        )
    category = SelectField(
        'Item Category',
        choices=ItemCategory.choices(),
        validators=[DataRequired()]
        )
    photo_url = StringField(
        'Item Picture',
        validators=[DataRequired(), URL()]
        )
    store = QuerySelectField(
        'Store Item is Located In',
        query_factory=lambda: GroceryStore.query
        )
    submit = SubmitField('Submit')
