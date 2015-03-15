var LanguageModel = Backbone.Model.extend ({

    urlRoot: '/api/language/',

    defaults: function() {
        return {
            title: ""
        }
    }
});