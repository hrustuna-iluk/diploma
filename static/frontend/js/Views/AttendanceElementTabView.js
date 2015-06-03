var AttendanceElementTabView = BaseView.extend({

    tagName: 'tr',

    template:  _.template($("#attendanceElementTabTemplate").html()),

    passes: [],

    month: [8, 9, 10, 11, 0, 1, 2, 3, 4, 5],

    initialize: function(options) {
        this.passesCollection = options.passesCollection;
    },

    _searchPasses: function() {
        var iter = 0, first = 0, second = 0;
        for(iter; iter <=9; iter++) {
            this.passesCollection.each($.proxy(function (model) {
                if(model.get('student').id === this.model.get('id') && this.month[iter] === new Date(model.get('date')).getMonth()
                && model.get('type') != 'pass'){
                first++;

                } else if(model.get('student').id === this.model.get('id')
                    && this.month[iter] === new Date(model.get('date')).getMonth()
                    && model.get('type') === 'pass') {
                    second++;
                } else {
                    return;
                }
            }, this));
            this.passes.push(first);
            this.passes.push(second);

            first = 0;
            second = 0;

        }
        console.log(this.passes);
    },

    render: function() {
        this._searchPasses();
        this.$el.html(this.template(_.extend(this.model.toJSON(), {passes: this.passes})));
        return this;
    }

});