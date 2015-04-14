var PaginationModel = Backbone.Model.extend({

    defaults: function() {
        return {
            number: 0,
            numberOfWeek: 0,
            start: null,
            end: null
        }
    }

});