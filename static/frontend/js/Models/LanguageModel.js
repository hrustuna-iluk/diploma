var LanguageModel = Backbone.Model.extend ({

    urlRoot: '/api/language/',

    defaults: function() {
        return {
            title: ""
        }
    },

    parse: function(resp) {
        if (_.isArray(resp)) {
            return resp[0];
        }
        return resp;
    }
});