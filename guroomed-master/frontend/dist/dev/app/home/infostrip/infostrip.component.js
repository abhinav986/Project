"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var InfostripComponent = (function () {
    function InfostripComponent() {
    }
    Object.defineProperty(InfostripComponent.prototype, "data", {
        get: function () { return this._data; },
        set: function (data) {
            this._data = (data) || [];
        },
        enumerable: true,
        configurable: true
    });
    InfostripComponent.prototype.ngOnInit = function () {
    };
    __decorate([
        core_1.Input(),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], InfostripComponent.prototype, "data", null);
    InfostripComponent = __decorate([
        core_1.Component({
            selector: 'app-infostrip',
            templateUrl: '../app/home/infostrip/infostrip.component.html',
            styleUrls: ['../app/home/infostrip/infostrip.component.css']
        }),
        __metadata("design:paramtypes", [])
    ], InfostripComponent);
    return InfostripComponent;
}());
exports.InfostripComponent = InfostripComponent;

//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImFwcC9ob21lL2luZm9zdHJpcC9pbmZvc3RyaXAuY29tcG9uZW50LnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7O0FBQUEsc0NBQXNFO0FBT3RFO0lBT0U7SUFBZ0IsQ0FBQztJQUpqQixzQkFBSSxvQ0FBSTthQUdSLGNBQWtCLE1BQU0sQ0FBQyxJQUFJLENBQUMsS0FBSyxDQUFDLENBQUMsQ0FBQzthQUh0QyxVQUFTLElBQVE7WUFDZixJQUFJLENBQUMsS0FBSyxHQUFHLENBQUMsSUFBSSxDQUFDLElBQUksRUFBRSxDQUFDO1FBQzVCLENBQUM7OztPQUFBO0lBS0QscUNBQVEsR0FBUjtJQUVBLENBQUM7SUFURDtRQURFLFlBQUssRUFBRTs7O2tEQUdSO0lBTFUsa0JBQWtCO1FBTDlCLGdCQUFTLENBQUM7WUFDVCxRQUFRLEVBQUUsZUFBZTtZQUN6QixXQUFXLEVBQUUsZ0RBQWdEO1lBQzdELFNBQVMsRUFBRSxDQUFDLCtDQUErQyxDQUFDO1NBQzdELENBQUM7O09BQ1csa0JBQWtCLENBYTlCO0lBQUQseUJBQUM7Q0FiRCxBQWFDLElBQUE7QUFiWSxnREFBa0IiLCJmaWxlIjoiYXBwL2hvbWUvaW5mb3N0cmlwL2luZm9zdHJpcC5jb21wb25lbnQuanMiLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBDb21wb25lbnQsIE9uSW5pdCxTaW1wbGVDaGFuZ2VzLElucHV0IH0gZnJvbSAnQGFuZ3VsYXIvY29yZSc7XHJcblxyXG5AQ29tcG9uZW50KHtcclxuICBzZWxlY3RvcjogJ2FwcC1pbmZvc3RyaXAnLFxyXG4gIHRlbXBsYXRlVXJsOiAnLi4vYXBwL2hvbWUvaW5mb3N0cmlwL2luZm9zdHJpcC5jb21wb25lbnQuaHRtbCcsXHJcbiAgc3R5bGVVcmxzOiBbJy4uL2FwcC9ob21lL2luZm9zdHJpcC9pbmZvc3RyaXAuY29tcG9uZW50LmNzcyddXHJcbn0pXHJcbmV4cG9ydCBjbGFzcyBJbmZvc3RyaXBDb21wb25lbnQgaW1wbGVtZW50cyBPbkluaXQge1xyXG4gIHByaXZhdGUgX2RhdGE6YW55O1xyXG4gICBASW5wdXQoKVxyXG4gIHNldCBkYXRhKGRhdGE6YW55KSB7XHJcbiAgICB0aGlzLl9kYXRhID0gKGRhdGEpIHx8IFtdO1xyXG4gIH1cclxuICBnZXQgZGF0YSgpOiBhbnkgeyByZXR1cm4gdGhpcy5fZGF0YTsgfVxyXG4gIGNvbnN0cnVjdG9yKCkgeyB9XHJcblxyXG5cclxuICBuZ09uSW5pdCgpIHtcclxuXHJcbiAgfVxyXG59XHJcbiJdfQ==
