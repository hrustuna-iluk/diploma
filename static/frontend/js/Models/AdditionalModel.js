var AdditionalModel = Backbone.Model.extend ({

    urlRoot: '/api/additional',

    defaults: function() {
        return {
            title: "",
            value: "",
            student: null
        }
    }

});