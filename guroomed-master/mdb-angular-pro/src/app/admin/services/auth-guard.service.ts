import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { ToastService } from '../../typescripts/pro';
import { AuthenticationService } from '../../services/authentication.service';

@Injectable()
export class AuthGuardService implements CanActivate {

  constructor(private autheService: AuthenticationService, private router: Router, private toastrService: ToastService) { }

  canActivate(): boolean {
    if (this.autheService.loggedIn()) {
      return true;
    } else {
      let options = { closeButton: true, tapToDismiss: true, positionClass: 'toast-top-right' };
      this.toastrService.error("", "Unauthorized access!", options);
      this.router.navigate(['']);
      return false;
    }
  }

}
