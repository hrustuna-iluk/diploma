var BenefitsModel = Backbone.Model.extend ({

    urlRoot: '/api/benefits/',

    defaults: function() {
        return {
            type: ""
        }
    },

    parse: function(resp) {
        if (_.isArray(resp)) {
            return resp[0];
        }
        return resp;
    }
});