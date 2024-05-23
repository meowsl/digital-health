export interface User {
  id: number | undefined
  firstName: string | undefined
  lastName: string | undefined
  username: string | undefined
  email: string | undefined
}

export interface AuthState {
  user: User | null
}

export interface JWTTokenDecode {
  sub: number
  exp: number
}
