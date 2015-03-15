var PublicOrdersCollection = Backbone.Collection.extend({

    url: "/api/publicOrders",

    model: PublicOrdersModel

});