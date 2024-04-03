#[no_mangle]
pub extern "C" fn bubble_sort(arr: *mut i32, len: usize) {
    // Assurer que le pointeur n'est pas null et que la longueur n'est pas nulle.
    if arr.is_null() || len == 0 {
        return;
    }

    // Convertir le pointeur brut en slice mutable pour faciliter le travail avec Rust.
    // C'est sûr à ce point grâce aux vérifications au-dessus.
    let arr = unsafe { std::slice::from_raw_parts_mut(arr, len) };

    let n = arr.len();
    for i in 0..n {
        for j in 0..n - i - 1 {
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1);
            }
        }
    }
}
