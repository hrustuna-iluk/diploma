var LanguagesCollection = Backbone.Collection.extend({

    url: "/api/languages",

    model: LanguageModel

});