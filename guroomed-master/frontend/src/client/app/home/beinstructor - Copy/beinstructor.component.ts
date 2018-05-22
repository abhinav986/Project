import { Component, OnInit,Input,SimpleChanges  } from '@angular/core';

@Component({
  selector: 'app-beinstructor',
  templateUrl: '../app/home/beinstructor/beinstructor.component.html',
  styleUrls: ['../app/home/beinstructor/beinstructor.component.css']
})
export class BeinstructorComponent implements OnInit {
	 @Input()
     data:any;


  constructor() { }
  ngOnChanges(changes: SimpleChanges) {
        // only run when property "data" changed
        if (changes['data']) {
            console.log(this.data);
        }
    }

  ngOnInit() {
  }

}
