import { Component, OnInit } from '@angular/core';
import { NavbarService } from 'app/shared/navbarService/navbar.service';
import { ActivatedRoute, Router } from '@angular/router';
import { CourseDetailService } from 'app/services/coursedetail/course-detail.service';
import { ShoppingcartService } from 'app/services/shopcart/shoppingcart.service';
import { LoaderService } from 'app/shared/loader/loader.service';
import { AuthenticationService } from '../services/authentication.service';
import { ToastService } from '../typescripts/pro';
import { InstructorServiceService } from '../become-instructor/instructor-service/instructor-service.service';

@Component({
  selector: 'app-course-detail',
  templateUrl: './course-detail.component.html',
  styleUrls: ['./course-detail.component.scss'],
})
export class CourseDetailComponent implements OnInit {
  instructorData: any;
  draftReference: string;
  goToCartButton: boolean;

  errorMessage: any;
  courseDetailsdata: string[];
  course_id: any;
  showed: boolean = false;
  private storage: Storage;
  options;
  image_url: string;

  constructor(
    private nav: NavbarService,
    private loader: LoaderService,
    private router: Router,
    private route: ActivatedRoute,
    private courseDetails: CourseDetailService,
    private shoppingCartService: ShoppingcartService,
    private authenticationService: AuthenticationService,
    private toastrService: ToastService,
    private instructorService: InstructorServiceService
  ) { }

  ngOnInit() {
    this.nav.show();
    this.loader.show();
    this.course_id = this.route.snapshot.params.id;
    this.draftReference = this.route.routeConfig.path;
    if (this.draftReference == 'instructor/course/draft-content/:id') {
     this.getInstructorDraftData();
    } else {
      this.courseData();
    }
    this.addedToCart(this.course_id);
    this.options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
  }

  getInstructorDraftData(){
    this.instructorService.getList(this.course_id).subscribe(instructorData => {
     this.instructorData = instructorData['draft'];
     this.loader.hide();
    });
  }
  
  courseData() {
    this.courseDetails.get(this.course_id)
      .subscribe(courseDetailsData => {
        this.courseDetailsdata = courseDetailsData;
        if (window.location.port == '4200') {
          this.image_url = 'http://127.0.0.1:8000' + this.courseDetailsdata['preview_image_url'];;
        } else {
          this.image_url = 'http://www.guroomed.com' + this.courseDetailsdata['preview_image_url'];;
        }
        this.loader.hide();
      },
        error => this.errorMessage = <any>error
      );
  }

  addToCart(courseData) {

    if (this.authenticationService.loggedIn()) {
      this.shoppingCartService.addItem(courseData)
        .subscribe(data => {
          if (data.status == 1) {
            this.goToCartButton = true;
            this.toastrService.success('', 'Course added to cart !', this.options);
          } else {
            this.goToCartButton = false;
          }
          this.shoppingCartService.cartCounter(data.count);
        });
    } else {
      this.shoppingCartService.addItem(courseData);
      this.toastrService.success('', 'Course added to cart !', this.options);
      this.addedToCart(courseData.id);
      var countItem = JSON.parse(localStorage.getItem('cart_key'));
      this.shoppingCartService.cartCounter(countItem.items.length);
    }

  }

  addedToCart(id) {
    if (localStorage.getItem('cart_key') != null) {
      this.storage = JSON.parse(localStorage.getItem('cart_key'));
      this.storage.items.find(element => {
        if (element.courseId == id) {
          return this.goToCartButton = true;
        } else {
          return this.goToCartButton = false;
        }
      });
    }

    if (this.authenticationService.loggedIn()) {
      this.shoppingCartService.getCartItem(localStorage.getItem('user_id'))
        .subscribe(data => {
          data['items'].find(element => {
            if (element.courseId == id) {
              return this.goToCartButton = true;
            } else {
              return this.goToCartButton = false;
            }
          });
        });
    }
  }

  // buyNow(course_id){
  //   if (this.authenticationService.loggedIn()) {
  //     this.router.navigate(['checkout']);
  //   } else {
  //     this.toastrService.info('', 'Please login to continue.... !', this.options);
  //   }
  // }

  goToCart() {
    this.router.navigate(['cart']);
  }


}
