var PublicPlanCollection = Backbone.Collection.extend({

    url: '/api/publicplans',

    model: PublicPlanModel

});