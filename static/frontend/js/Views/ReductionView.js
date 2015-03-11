var ReductionView = BaseView.extend ({

    template:  _.template($("#reductionTemplate").html()),

    initialize: function(options) {
        this.model = new AttendanceModel ({
           group: options.group
        });
    },

    _attachEvents: function() {
    },

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        this._attachEvents();
        return this;
    }

});