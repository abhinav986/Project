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
var ForbusinessComponent = (function () {
    function ForbusinessComponent() {
    }
    Object.defineProperty(ForbusinessComponent.prototype, "data", {
        get: function () { return this._data; },
        set: function (data) {
            this._data = (data) || { name: "peace" };
        },
        enumerable: true,
        configurable: true
    });
    ForbusinessComponent.prototype.ngOnInit = function () {
    };
    __decorate([
        core_1.Input(),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], ForbusinessComponent.prototype, "data", null);
    ForbusinessComponent = __decorate([
        core_1.Component({
            selector: 'app-forbusiness',
            templateUrl: '../app/home/forbusiness/forbusiness.component.html',
            styleUrls: ['../app/home/forbusiness/forbusiness.component.css']
        }),
        __metadata("design:paramtypes", [])
    ], ForbusinessComponent);
    return ForbusinessComponent;
}());
exports.ForbusinessComponent = ForbusinessComponent;

//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImFwcC9ob21lL2ZvcmJ1c2luZXNzL2ZvcmJ1c2luZXNzLmNvbXBvbmVudC50cyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7OztBQUFBLHNDQUF1RTtBQU92RTtJQVNFO0lBQWdCLENBQUM7SUFMakIsc0JBQUksc0NBQUk7YUFHUixjQUFrQixNQUFNLENBQUMsSUFBSSxDQUFDLEtBQUssQ0FBQyxDQUFDLENBQUM7YUFIdEMsVUFBUyxJQUFRO1lBQ2YsSUFBSSxDQUFDLEtBQUssR0FBRyxDQUFDLElBQUksQ0FBQyxJQUFJLEVBQUMsSUFBSSxFQUFDLE9BQU8sRUFBQyxDQUFDO1FBQ3hDLENBQUM7OztPQUFBO0lBS0QsdUNBQVEsR0FBUjtJQUNBLENBQUM7SUFSRDtRQURDLFlBQUssRUFBRTs7O29EQUdQO0lBTlUsb0JBQW9CO1FBTGhDLGdCQUFTLENBQUM7WUFDVCxRQUFRLEVBQUUsaUJBQWlCO1lBQzNCLFdBQVcsRUFBRSxvREFBb0Q7WUFDakUsU0FBUyxFQUFFLENBQUMsbURBQW1ELENBQUM7U0FDakUsQ0FBQzs7T0FDVyxvQkFBb0IsQ0FhaEM7SUFBRCwyQkFBQztDQWJELEFBYUMsSUFBQTtBQWJZLG9EQUFvQiIsImZpbGUiOiJhcHAvaG9tZS9mb3JidXNpbmVzcy9mb3JidXNpbmVzcy5jb21wb25lbnQuanMiLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBDb21wb25lbnQsIE9uSW5pdCwgU2ltcGxlQ2hhbmdlcyxJbnB1dCB9IGZyb20gJ0Bhbmd1bGFyL2NvcmUnO1xyXG5cclxuQENvbXBvbmVudCh7XHJcbiAgc2VsZWN0b3I6ICdhcHAtZm9yYnVzaW5lc3MnLFxyXG4gIHRlbXBsYXRlVXJsOiAnLi4vYXBwL2hvbWUvZm9yYnVzaW5lc3MvZm9yYnVzaW5lc3MuY29tcG9uZW50Lmh0bWwnLFxyXG4gIHN0eWxlVXJsczogWycuLi9hcHAvaG9tZS9mb3JidXNpbmVzcy9mb3JidXNpbmVzcy5jb21wb25lbnQuY3NzJ11cclxufSlcclxuZXhwb3J0IGNsYXNzIEZvcmJ1c2luZXNzQ29tcG9uZW50IGltcGxlbWVudHMgT25Jbml0IHtcclxuXHJcbiBfZGF0YTphbnk7XHJcbiAgQElucHV0KClcclxuICBzZXQgZGF0YShkYXRhOmFueSkge1xyXG4gICAgdGhpcy5fZGF0YSA9IChkYXRhKSB8fCB7bmFtZTpcInBlYWNlXCJ9O1xyXG4gIH1cclxuICBnZXQgZGF0YSgpOiBhbnkgeyByZXR1cm4gdGhpcy5fZGF0YTsgfVxyXG4gICAgIFxyXG4gIGNvbnN0cnVjdG9yKCkgeyB9XHJcblxyXG4gIG5nT25Jbml0KCkge1xyXG4gIH1cclxufVxyXG4iXX0=
