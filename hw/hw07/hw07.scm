(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond
    ((> num 0) 1)
    ((< num 0) -1)
    ((= num 0) 0))
)


(define (square x) (* x x))

(define (pow x y)
  ; (if (= y 0) 1)
  ; (if (= y 1) x
  ;   (if (even? y)
  ;     (square (pow x (/ y 2))))
  ;     (* x (square (pow x (floor (/ y 2)))))
  ; )
  (if (= y 1) x
        (if (even? y) 
            (square (pow x (/ y 2)))
            (* x (square (pow x (floor (/ y 2)))))
        )
    )
)


(define (unique s)
  (if (null? s) s
  (cons (car s) (unique (filter (lambda (x) (not(equal? x (car s))) ) (cdr s))))
  )
)


(define (replicate x n)
  (define (replicate_tail_recursive x s n)
    (if (= n 0) s
      (replicate_tail_recursive x (cons x s) (- n 1))
      )
    )
  (replicate_tail_recursive x nil n)
  )


(define (accumulate combiner start n term)
  (define (accumu_helper combiner start n term)
    (if (= 0 n) start
      (accumu_helper combiner (combiner start (term n)) (- n 1) term)
      )
    )
  (accumu_helper combiner start n term)
)

; I don't want to rewrite the traditional recursive func again...
(define (accumulate-tail combiner start n term)
  (define (accumu_helper combiner start n term)
    (if (= 0 n) start
      (accumu_helper combiner (combiner start (term n)) (- n 1) term)
      )
    )
  (accumu_helper combiner start n term)
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)

