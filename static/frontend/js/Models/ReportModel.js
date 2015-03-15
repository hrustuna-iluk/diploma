var ReportModel = Backbone.Model.extend ({

    urlRoot: '/api/report/',

    defaults: function() {
        return {
            date: "",
            event: EventModel
        }
    }
});