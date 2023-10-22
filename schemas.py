from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    
# user
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    role = fields.Str(required=True) 
    
class LoginUserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    
class PlainAddressSchema(Schema):
    id = fields.Int(dump_only=True)
    city = fields.Str(required=True)
    street = fields.Str(required=True)  
    
class PlainAuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    
class AddressSchema(PlainAddressSchema):
    author = fields.Nested(PlainAuthorSchema(), dump_only=True)
    
class AuthorSchema(PlainAuthorSchema):
    address_id = fields.Int(required=True, load_only=True)
    address = fields.Nested(PlainAddressSchema(), dump_only=True)
    books = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)   



class PlainBookSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    
    
class PlainCountrySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainIdSchema(Schema):
    id = fields.Int(dump_only=True)
    
class PlainCountryIdSchema(Schema):
    country_id = fields.Nested(PlainIdSchema)
    
class CountrySchema(PlainCountrySchema):
    books = fields.List(fields.Nested(PlainBookSchema()), dump_only=True)  

class BookSchema(PlainBookSchema):
    # author_id = fields.Int(required=True, load_only=True)
    author_id = fields.Int(required=True, load_only=True)
    author = fields.Nested(PlainAuthorSchema(), dump_only=True)
    countries = fields.List(fields.Nested(PlainCountrySchema()), dump_only=True)
    country_id = fields.List(fields.Int(), load_only=True)