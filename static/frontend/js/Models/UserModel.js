var UserModel = Backbone.Model.extend({

    urlRoot: "",

    defaults: function() {
        return {
            username: "",
            password: "",
            isActive: false
        }
    }
});