var BenefitsModel = Backbone.Model.extend ({

    urlRoot: '/api/benefits',

    defaults: function() {
        return {
            type: ""
        }
    }
});