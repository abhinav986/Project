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
    BeinstructorComponent.prototype.ngOnChanges = function (changes) {
        if (changes['data']) {
            console.log(this.data);
        }
    };
    BeinstructorComponent.prototype.ngOnInit = function () {
    };
    __decorate([
        core_1.Input(),
        __metadata("design:type", Object)
    ], BeinstructorComponent.prototype, "data", void 0);
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

//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImFwcC9ob21lL2JlaW5zdHJ1Y3RvciAtIENvcHkvYmVpbnN0cnVjdG9yLmNvbXBvbmVudC50cyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7OztBQUFBLHNDQUF1RTtBQU92RTtJQUtFO0lBQWdCLENBQUM7SUFDakIsMkNBQVcsR0FBWCxVQUFZLE9BQXNCO1FBRTVCLEVBQUUsQ0FBQyxDQUFDLE9BQU8sQ0FBQyxNQUFNLENBQUMsQ0FBQyxDQUFDLENBQUM7WUFDbEIsT0FBTyxDQUFDLEdBQUcsQ0FBQyxJQUFJLENBQUMsSUFBSSxDQUFDLENBQUM7UUFDM0IsQ0FBQztJQUNMLENBQUM7SUFFSCx3Q0FBUSxHQUFSO0lBQ0EsQ0FBQztJQVpFO1FBREYsWUFBSyxFQUFFOzt1REFDSTtJQUZELHFCQUFxQjtRQUxqQyxnQkFBUyxDQUFDO1lBQ1QsUUFBUSxFQUFFLGtCQUFrQjtZQUM1QixXQUFXLEVBQUUsc0RBQXNEO1lBQ25FLFNBQVMsRUFBRSxDQUFDLHFEQUFxRCxDQUFDO1NBQ25FLENBQUM7O09BQ1cscUJBQXFCLENBZ0JqQztJQUFELDRCQUFDO0NBaEJELEFBZ0JDLElBQUE7QUFoQlksc0RBQXFCIiwiZmlsZSI6ImFwcC9ob21lL2JlaW5zdHJ1Y3RvciAtIENvcHkvYmVpbnN0cnVjdG9yLmNvbXBvbmVudC5qcyIsInNvdXJjZXNDb250ZW50IjpbImltcG9ydCB7IENvbXBvbmVudCwgT25Jbml0LElucHV0LFNpbXBsZUNoYW5nZXMgIH0gZnJvbSAnQGFuZ3VsYXIvY29yZSc7XHJcblxyXG5AQ29tcG9uZW50KHtcclxuICBzZWxlY3RvcjogJ2FwcC1iZWluc3RydWN0b3InLFxyXG4gIHRlbXBsYXRlVXJsOiAnLi4vYXBwL2hvbWUvYmVpbnN0cnVjdG9yL2JlaW5zdHJ1Y3Rvci5jb21wb25lbnQuaHRtbCcsXHJcbiAgc3R5bGVVcmxzOiBbJy4uL2FwcC9ob21lL2JlaW5zdHJ1Y3Rvci9iZWluc3RydWN0b3IuY29tcG9uZW50LmNzcyddXHJcbn0pXHJcbmV4cG9ydCBjbGFzcyBCZWluc3RydWN0b3JDb21wb25lbnQgaW1wbGVtZW50cyBPbkluaXQge1xyXG5cdCBASW5wdXQoKVxyXG4gICAgIGRhdGE6YW55O1xyXG5cclxuXHJcbiAgY29uc3RydWN0b3IoKSB7IH1cclxuICBuZ09uQ2hhbmdlcyhjaGFuZ2VzOiBTaW1wbGVDaGFuZ2VzKSB7XHJcbiAgICAgICAgLy8gb25seSBydW4gd2hlbiBwcm9wZXJ0eSBcImRhdGFcIiBjaGFuZ2VkXHJcbiAgICAgICAgaWYgKGNoYW5nZXNbJ2RhdGEnXSkge1xyXG4gICAgICAgICAgICBjb25zb2xlLmxvZyh0aGlzLmRhdGEpO1xyXG4gICAgICAgIH1cclxuICAgIH1cclxuXHJcbiAgbmdPbkluaXQoKSB7XHJcbiAgfVxyXG5cclxufVxyXG4iXX0=
