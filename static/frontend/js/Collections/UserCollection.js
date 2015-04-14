var UserCollection = Backbone.Collection.extend({

    url: "/api/users",

    model: UserModel

});