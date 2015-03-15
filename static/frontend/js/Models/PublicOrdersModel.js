var PublicOrdersModel = Backbone.Model.extend ({

    urlRoot: '/api/publicorders/',

    defaults: function() {
        return {
            type: ""
        }
    }
});