var PaginationsView  = BaseView.extend({

    tagName: "ul",

    className: "pagination",

    initialize: function() {
        this.collection = new PaginationCollection();
    },

    _addPaginationElement: function() {

    },

    render: function() {
        this._addPaginationElement();
        return this;
    }

});