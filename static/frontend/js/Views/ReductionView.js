var ReductionView = BaseView.extend ({

    template:  _.template($("#reductionTemplate").html()),

    initialize: function(options) {
        this.group = options.group;
        this.model = options.model;
    },

    _attachEvents: function() {
    },

    render: function() {
        this.$el.html(this.template(_.extend(this.model.toJSON(), this.group.toJSON())));
        this._attachEvents();
        return this;
    }

});