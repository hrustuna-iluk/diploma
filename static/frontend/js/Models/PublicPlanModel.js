var PublicPlanModel = Backbone.Model.extend ({

    urlRoot: '/api/publicplan',

    defaults: function() {
        return {
            event: EventModel,
            date: 0,
            responsive: "",
            description: "",
            amountHours: 0,
            amountPresent: 0
        }
    }

});