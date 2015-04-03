var ClassesView = BaseView.extend ({

    tagName: 'tr',

    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],

    initialize: function(options) {
        this.numberOfClass = options.numberOfClass;
        this.group = options.group;
        this.collection = options.collection;
        this.numberOfWeek = options.numberOfWeek;
        this.scheduleModel = options.scheduleModel;
        this.teachersCollection = options.teachersCollection;
    },

    _buildRow: function() {
        if(!this.collection.length) {
            this.days.forEach($.proxy(function (weekDay, index, array) {
               var model = new ClassModel({
                   group: this.group.get('id'),
                   day: weekDay,
                   number: this.numberOfClass,
                   numberOfWeek: this.numberOfWeek,
                   schedule: this.scheduleModel
               });
               this.$el.append(
                   new ClassView({
                       group: this.group,
                       model: model,
                       teachersCollection: this.teachersCollection
                   }).render().$el
               );
            }, this));
        }
    },

    render: function() {
        this._buildRow();
        return this;
    }
});