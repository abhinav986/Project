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
var BeinstructorComponent = (function () {
    function BeinstructorComponent() {
    }
    Object.defineProperty(BeinstructorComponent.prototype, "data", {
        get: function () { return this._data; },
        set: function (data) {
            this._data = (data) || { name: "peace" };
        },
        enumerable: true,
        configurable: true
    });
    BeinstructorComponent.prototype.ngOnInit = function () {
    };
    __decorate([
        core_1.Input(),
        __metadata("design:type", Object),
        __metadata("design:paramtypes", [Object])
    ], BeinstructorComponent.prototype, "data", null);
    BeinstructorComponent = __decorate([
        core_1.Component({
            selector: 'app-beinstructor',
            templateUrl: '../app/home/beinstructor/beinstructor.component.html',
            styleUrls: ['../app/home/beinstructor/beinstructor.component.css']
        }),
        __metadata("design:paramtypes", [])
    ], BeinstructorComponent);
    return BeinstructorComponent;
}());
exports.BeinstructorComponent = BeinstructorComponent;

//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImFwcC9ob21lL2JlaW5zdHJ1Y3Rvci9iZWluc3RydWN0b3IuY29tcG9uZW50LnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7O0FBQUEsc0NBQXVFO0FBT3ZFO0lBUUU7SUFBZ0IsQ0FBQztJQUxqQixzQkFBSSx1Q0FBSTthQUdSLGNBQWtCLE1BQU0sQ0FBQyxJQUFJLENBQUMsS0FBSyxDQUFDLENBQUMsQ0FBQzthQUh0QyxVQUFTLElBQVE7WUFDZixJQUFJLENBQUMsS0FBSyxHQUFHLENBQUMsSUFBSSxDQUFDLElBQUksRUFBQyxJQUFJLEVBQUMsT0FBTyxFQUFDLENBQUM7UUFDeEMsQ0FBQzs7O09BQUE7SUFLRCx3Q0FBUSxHQUFSO0lBQ0EsQ0FBQztJQVJEO1FBREMsWUFBSyxFQUFFOzs7cURBR1A7SUFMVSxxQkFBcUI7UUFMakMsZ0JBQVMsQ0FBQztZQUNULFFBQVEsRUFBRSxrQkFBa0I7WUFDNUIsV0FBVyxFQUFFLHNEQUFzRDtZQUNuRSxTQUFTLEVBQUUsQ0FBQyxxREFBcUQsQ0FBQztTQUNuRSxDQUFDOztPQUNXLHFCQUFxQixDQWFqQztJQUFELDRCQUFDO0NBYkQsQUFhQyxJQUFBO0FBYlksc0RBQXFCIiwiZmlsZSI6ImFwcC9ob21lL2JlaW5zdHJ1Y3Rvci9iZWluc3RydWN0b3IuY29tcG9uZW50LmpzIiwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgQ29tcG9uZW50LCBPbkluaXQsSW5wdXQsU2ltcGxlQ2hhbmdlcyAgfSBmcm9tICdAYW5ndWxhci9jb3JlJztcclxuXHJcbkBDb21wb25lbnQoe1xyXG4gIHNlbGVjdG9yOiAnYXBwLWJlaW5zdHJ1Y3RvcicsXHJcbiAgdGVtcGxhdGVVcmw6ICcuLi9hcHAvaG9tZS9iZWluc3RydWN0b3IvYmVpbnN0cnVjdG9yLmNvbXBvbmVudC5odG1sJyxcclxuICBzdHlsZVVybHM6IFsnLi4vYXBwL2hvbWUvYmVpbnN0cnVjdG9yL2JlaW5zdHJ1Y3Rvci5jb21wb25lbnQuY3NzJ11cclxufSlcclxuZXhwb3J0IGNsYXNzIEJlaW5zdHJ1Y3RvckNvbXBvbmVudCBpbXBsZW1lbnRzIE9uSW5pdCB7XHJcblx0X2RhdGE6YW55O1xyXG4gIEBJbnB1dCgpXHJcbiAgc2V0IGRhdGEoZGF0YTphbnkpIHtcclxuICAgIHRoaXMuX2RhdGEgPSAoZGF0YSkgfHwge25hbWU6XCJwZWFjZVwifTtcclxuICB9XHJcbiAgZ2V0IGRhdGEoKTogYW55IHsgcmV0dXJuIHRoaXMuX2RhdGE7IH1cclxuXHJcbiAgY29uc3RydWN0b3IoKSB7IH1cclxuXHJcbiAgbmdPbkluaXQoKSB7XHJcbiAgfVxyXG5cclxufVxyXG4iXX0=
