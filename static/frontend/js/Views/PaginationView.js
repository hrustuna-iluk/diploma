var PaginationView = BaseView.extend({

    initialize: function(options) {
        this.collection = options.collection;
        this._addPaginationModel();
    },

    

    _countStart: function() {},

    _countEnd: function() {},

    _countWeek: function() {
    },

    _addPaginationModel: function() {
        this.model = new PaginationModel({
            number: this.collection.length() + 1
        });
        this.collection.add(this.model);
    },

    render: function() {
        this.$el.html();
        return this;
    }

});