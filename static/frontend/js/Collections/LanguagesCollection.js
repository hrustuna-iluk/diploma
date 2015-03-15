var LanguagesCollection = Backbone.Collection.extend({

    url: "/api/languages",

    model: LanguageModel,

    parse: function (response) {
        var result = [];

        response = JSON.parse(response);
        _.each(response, function (item) {
            item = _.extend({
                id: item['pk']
            }, item['fields']);
            result.push(item);
        });
        return result;
    }

});