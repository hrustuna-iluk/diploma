var ClassroomModel = Backbone.Model.extend ({

    urlRoot: '/api/classroom',

    defaults: function() {
        return {
            number: ""
        }
    }

});