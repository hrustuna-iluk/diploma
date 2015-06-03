var AttendanceView = BaseView.extend({

    template:  _.template($("#attendanceTabTemplate").html()),

    initialize: function(options) {
        this.studentsCollection = options.studentsCollection;
        this.passesCollection = options.passesCollection;
    },

    _fillTable: function() {
        this.studentsCollection.each($.proxy(function (model) {
            this.$('tbody').append(
            new AttendanceElementTabView({
                model: model,
                passesCollection: this.passesCollection
            }).render().el
            );
        }, this));
    },

    render: function() {
        this.$el.html(this.template());
        this._fillTable();
        return this;
    }

});