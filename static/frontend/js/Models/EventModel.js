var EventModel = Backbone.Model.extend({

    urlRoot: '/api/event',

    defaults: function() {
        return {
            title: ""
        }
    }
});