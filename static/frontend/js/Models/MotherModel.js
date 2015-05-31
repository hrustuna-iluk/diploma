var MotherModel = Backbone.Model.extend ({

    urlRoot: '/api/parents/',

    defaults: function() {
       return{
           fullName: "",
           phone: "",
           position: ""
       }
    },

    parse: function(resp) {
        if (_.isArray(resp)) {
            return resp[0];
        }
        return resp;
    }
});