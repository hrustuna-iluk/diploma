var BenefitsCollection = Backbone.Collection.extend({

    url: "/api/benefits",

    model: BenefitsModel
});