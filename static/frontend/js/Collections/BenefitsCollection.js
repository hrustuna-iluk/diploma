var BenefitsCollection = Backbone.Collection.extend({

    url: "/api/benefits",

    model: BenefitsModel,

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