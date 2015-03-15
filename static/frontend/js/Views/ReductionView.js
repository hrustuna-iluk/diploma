var ReductionView = BaseView.extend ({

    template:  _.template($("#reductionTemplate").html()),

    initialize: function(options) {
        this.model = options.model;
    },

    _attachEvents: function() {
    },

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        this._attachEvents();
        return this;
    }

});