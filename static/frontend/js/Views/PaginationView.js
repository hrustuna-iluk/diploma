var PaginationView = BaseView.extend({

    initialize: function(options) {
        this.collection = options.collection;
        this._addPaginationModel();
    },



    _countStart: function() {},

    _countEnd: function() {},

    _countWeek: function() {
        if((this.collection.length+1)%2){
            return 2;
        }else{
            return 1;
        }
    },

    _addPaginationModel: function() {
        var week = this._countWeek();
        this.model = new PaginationModel({
            number: this.collection.length + 1,
            numberOfWeek: week
        });
        this.collection.add(this.model);
    },

    render: function() {
        this.$el.html();
        return this;
    }

});