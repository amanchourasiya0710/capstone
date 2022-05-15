import {
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    USER_LOADED_SUCCESS,
    USER_LOADED_FAIL,

    AUTHENTICATED_SUCCESS,
    AUTHENTICATED_FAIL,
    LOGOUT,

    PASSWORD_RESET_SUCCESS,
    PASSWORD_RESET_FAIL,
    PASSWORD_RESET_CONFIRM_SUCCESS,
    PASSWORD_RESET_CONFIRM_FAIL,

    SIGNUP_SUCCESS,
    SIGNUP_FAIL,
    ACTIVATION_SUCCESS,
    ACTIVATION_FAIL,
} from "../actions/types";

const initialState = {
  access: localStorage.getItem("access"),
  refresh: localStorage.getItem("refresh"),
  isAuthenticated: null,
  user: null,
};

export default function (state = initialState, action) {
  const { type, payload } = action;

  switch (type) {
    case AUTHENTICATED_SUCCESS:
        return {
            ...state,
            isAuthenticated: true
        }
    case LOGIN_SUCCESS:
        localStorage.setItem("access", payload.access);
        localStorage.setItem("refresh", payload.refresh);
        return {
            ...state,
            isAuthenticated: true,
            access: payload.access,
            refresh: payload.refresh,
        };
    case USER_LOADED_SUCCESS:
        return {
            ...state,
            user: payload,
            isAuthenticated: true,
        };
    case SIGNUP_SUCCESS:
    case AUTHENTICATED_FAIL:
        localStorage.setItem("access", null);
        localStorage.setItem("refresh", null);
        localStorage.setItem("email", null);
        return {
            ...state,
            access: null,
            refresh: null,
            isAuthenticated: false,
            user: null,
        }
    case USER_LOADED_FAIL:
        localStorage.setItem("access", null);
        localStorage.setItem("refresh", null);
        localStorage.setItem("email", null);
        return {
            ...state,
            access: null,
            refresh: null,
            isAuthenticated: false,
            user: null,
        };
    case LOGIN_FAIL:
    case SIGNUP_FAIL:
    case LOGOUT:
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        localStorage.setItem("email", null);
        return {
            ...state,
            access: null,
            refresh: null,
            isAuthenticated: false,
            user: null,
        };
    case PASSWORD_RESET_SUCCESS:
    case PASSWORD_RESET_FAIL:
    case PASSWORD_RESET_CONFIRM_SUCCESS:
    case PASSWORD_RESET_CONFIRM_FAIL:
    case ACTIVATION_SUCCESS:
    case ACTIVATION_FAIL:
        return {
            ...state
        }
    default:
        return state;
  }
}
